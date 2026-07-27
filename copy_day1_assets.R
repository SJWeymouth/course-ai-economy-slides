# copy_day1_assets.R
# Copy only the image files referenced by the Day 1 Quarto deck
# from a large Dropbox image library into this repository's assets/ folder.

# ---- Settings you may change ----
deck_path <- file.path("slides", "day1", "ai-intuition-progress.qmd")
assets_dir <- "assets"

# Option 1: set the Dropbox folder here, for example:
# source_dir <- "C:/Users/Stephen/Dropbox/Teaching/Images"
#
# Option 2: leave this blank and the script will ask you for the folder.
source_dir <- ""

# ---- Fallback list used if the .qmd file is not yet in the repository ----
fallback_assets <- c(
  "AI_graphic.png",
  "agents.jpeg",
  "ai_evolution.png",
  "ai_harm_survey.png",
  "altman1.png",
  "baldwin_holy_cow.png",
  "basel_2025_teams.png",
  "big_blue.jpg",
  "car_collage.jpg",
  "china_label.jpg",
  "compute.jpg",
  "deep_learning_subset.png",
  "dl_face.png",
  "equation.png",
  "go.png",
  "gpt4advances.png",
  "gpt_explainer.png",
  "iphone_apollo.png",
  "ml_code.png",
  "moores.png",
  "neural_net.jpeg",
  "neural_net_training.png",
  "neural_russell.png",
  "ng.jpg",
  "pixels.png",
  "prediction.png",
  "processing.png",
  "rometty1.jpeg",
  "sedol.jpg",
  "stanford_hai_24.png",
  "tail.jpg",
  "tesla.jpg",
  "turing_bbc_greatest.jpg",
  "turing_paper.png",
  "turing_test_diagram.png",
  "watson.jpg",
  "wave_cover.jpg"
)

extract_asset_names <- function(path) {
  if (!file.exists(path)) {
    message("Deck not found at: ", path)
    message("Using the embedded fallback asset list.")
    return(fallback_assets)
  }

  txt <- readLines(path, warn = FALSE, encoding = "UTF-8")

  # Match /assets/file.ext, ../../assets/file.ext, and similar relative forms.
  pattern <- "(?:^|[\\(\"'])((?:\\.\\./)*/?assets/[^\\)\"'[:space:]{}]+)"
  hits <- regmatches(txt, gregexpr(pattern, txt, perl = TRUE))
  hits <- unlist(hits, use.names = FALSE)

  if (length(hits) == 0) {
    message("No asset references were detected in the deck.")
    message("Using the embedded fallback asset list.")
    return(fallback_assets)
  }

  # Remove any leading punctuation, then keep only the filename below assets/.
  hits <- sub("^[\\(\"']+", "", hits)
  names <- sub("^.*assets/", "", hits)
  names <- sub("[?#].*$", "", names)
  unique(names[nzchar(names)])
}

if (!nzchar(source_dir)) {
  source_dir <- readline(
    paste0(
      "Paste the full path to your Dropbox images folder,\n",
      "then press Enter:\n> "
    )
  )
}

source_dir <- trimws(gsub('^"|"$', "", source_dir))

if (!dir.exists(source_dir)) {
  stop("The Dropbox source folder does not exist: ", source_dir)
}

dir.create(assets_dir, recursive = TRUE, showWarnings = FALSE)

required <- extract_asset_names(deck_path)
required <- unique(basename(required))

message("\nSearching recursively for ", length(required), " referenced files...")
message("Source: ", normalizePath(source_dir, winslash = "/", mustWork = TRUE))
message("Destination: ", normalizePath(assets_dir, winslash = "/", mustWork = TRUE))

all_files <- list.files(
  source_dir,
  recursive = TRUE,
  full.names = TRUE,
  include.dirs = FALSE,
  no.. = TRUE
)

# Case-insensitive lookup by filename.
lookup <- split(all_files, tolower(basename(all_files)))

results <- vector("list", length(required))

for (i in seq_along(required)) {
  target_name <- required[[i]]
  candidates <- lookup[[tolower(target_name)]]

  if (is.null(candidates) || length(candidates) == 0) {
    results[[i]] <- data.frame(
      required_file = target_name,
      status = "MISSING",
      chosen_source = "",
      destination = "",
      duplicate_count = 0L,
      all_candidates = "",
      stringsAsFactors = FALSE
    )
    next
  }

  # Prefer an exact case-sensitive filename match.
  exact <- candidates[basename(candidates) == target_name]

  if (length(exact) == 1) {
    chosen <- exact
  } else {
    pool <- if (length(exact) > 1) exact else candidates

    # If duplicates remain, choose the most recently modified copy.
    info <- file.info(pool)
    chosen <- pool[which.max(info$mtime)]
  }

  destination <- file.path(assets_dir, target_name)
  copied <- file.copy(chosen, destination, overwrite = TRUE, copy.date = TRUE)

  results[[i]] <- data.frame(
    required_file = target_name,
    status = if (copied) "COPIED" else "COPY FAILED",
    chosen_source = normalizePath(chosen, winslash = "/", mustWork = FALSE),
    destination = normalizePath(destination, winslash = "/", mustWork = FALSE),
    duplicate_count = length(candidates),
    all_candidates = paste(
      normalizePath(candidates, winslash = "/", mustWork = FALSE),
      collapse = " | "
    ),
    stringsAsFactors = FALSE
  )
}

report <- do.call(rbind, results)
report_path <- "asset_copy_report.csv"
write.csv(report, report_path, row.names = FALSE, fileEncoding = "UTF-8")

copied_n <- sum(report$status == "COPIED")
missing_n <- sum(report$status == "MISSING")
failed_n <- sum(report$status == "COPY FAILED")
duplicates_n <- sum(report$duplicate_count > 1)

cat("\nFinished.\n")
cat("Copied:    ", copied_n, "\n", sep = "")
cat("Missing:   ", missing_n, "\n", sep = "")
cat("Failed:    ", failed_n, "\n", sep = "")
cat("Duplicates:", duplicates_n, "\n", sep = "")
cat("Report:    ", normalizePath(report_path, winslash = "/", mustWork = FALSE), "\n", sep = "")

if (missing_n > 0) {
  cat("\nMissing files:\n")
  cat(paste0("  - ", report$required_file[report$status == "MISSING"]), sep = "\n")
  cat("\n")
}

if (duplicates_n > 0) {
  cat("\nSome filenames appeared more than once. The newest copy was selected unless\n")
  cat("there was a unique exact-case match. Review asset_copy_report.csv if needed.\n")
}

cat("\nNext steps:\n")
cat("1. Render slides/day1/ai-intuition-progress.qmd in RStudio.\n")
cat("2. Review the deck for missing or incorrect images.\n")
cat("3. Commit and push the .qmd plus assets/ files to GitHub.\n")
