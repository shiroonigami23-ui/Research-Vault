param(
  [Parameter(Mandatory=$true)]
  [ValidateSet('hollow_purple_semantic_nullification','judgment_chain_linguistic_smart_contracts','alluka_something_algorithmic_debt')]
  [string]$Paper
)

$paperPath = Join-Path $PSScriptRoot $Paper
Push-Location $paperPath
try {
  pdflatex main.tex
  bibtex main
  pdflatex main.tex
  pdflatex main.tex
}
finally {
  Pop-Location
}
