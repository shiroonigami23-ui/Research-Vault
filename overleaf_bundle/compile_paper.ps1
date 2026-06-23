param(
  [Parameter(Mandatory=$true)]
  [ValidateSet('hollow_purple_semantic_nullification','judgment_chain_linguistic_smart_contracts','alluka_something_algorithmic_debt')]
  [string]$Paper
)

$pdflatex = Get-Command pdflatex -ErrorAction SilentlyContinue
$bibtex = Get-Command bibtex -ErrorAction SilentlyContinue
if (-not $pdflatex) {
  $candidate = Join-Path $env:LOCALAPPDATA 'Programs\\MiKTeX\\miktex\\bin\\x64\\pdflatex.exe'
  if (Test-Path $candidate) { $pdflatex = @{ Source = $candidate } }
}
if (-not $bibtex) {
  $candidate = Join-Path $env:LOCALAPPDATA 'Programs\\MiKTeX\\miktex\\bin\\x64\\bibtex.exe'
  if (Test-Path $candidate) { $bibtex = @{ Source = $candidate } }
}
if (-not $pdflatex -or -not $bibtex) {
  throw 'pdflatex/bibtex not found. Install MiKTeX or another LaTeX distribution first.'
}

$paperPath = Join-Path $PSScriptRoot $Paper
Push-Location $paperPath
try {
  & $pdflatex.Source main.tex
  & $bibtex.Source main
  & $pdflatex.Source main.tex
  & $pdflatex.Source main.tex
}
finally {
  Pop-Location
}
