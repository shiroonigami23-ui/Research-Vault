param(
  [string]$TexFile = 'main.tex'
)
$pdflatex = Get-Command pdflatex -ErrorAction SilentlyContinue
$bibtex = Get-Command bibtex -ErrorAction SilentlyContinue
if (-not $pdflatex) {
  $candidate = Join-Path $env:LOCALAPPDATA 'Programs\MiKTeX\miktex\bin\x64\pdflatex.exe'
  if (Test-Path $candidate) { $pdflatex = @{ Source = $candidate } }
}
if (-not $bibtex) {
  $candidate = Join-Path $env:LOCALAPPDATA 'Programs\MiKTeX\miktex\bin\x64\bibtex.exe'
  if (Test-Path $candidate) { $bibtex = @{ Source = $candidate } }
}
if (-not $pdflatex -or -not $bibtex) { throw 'pdflatex/bibtex not found.' }
& $pdflatex.Source $TexFile
& $bibtex.Source ($TexFile -replace '\.tex$','')
& $pdflatex.Source $TexFile
& $pdflatex.Source $TexFile
