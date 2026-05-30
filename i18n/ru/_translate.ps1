param([string]$src = "C:\CoAsKB\i18n\en", [string]$dst = "C:\CoAsKB\i18n\ru")

# Copy structure
if (-not (Test-Path "$dst\skills")) { New-Item -ItemType Directory "$dst\skills" -Force | Out-Null }
Get-ChildItem "$src\skills" -Directory | ForEach-Object {
    $name = $_.Name
    $d = "$dst\skills\$name"
    if (-not (Test-Path $d)) { New-Item -ItemType Directory $d -Force | Out-Null }
    if (Test-Path "$src\skills\$name\SKILL.md") { Copy-Item "$src\skills\$name\SKILL.md" "$d\SKILL.md" -Force }
}
Copy-Item "$src\shared-references\*" "$dst\shared-references\" -Force
