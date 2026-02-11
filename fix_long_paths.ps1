# Check for Administrator privileges
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Warning "This script must be run as Administrator."
    exit
}

# Enable Long Paths in Registry
$RegistryPath = "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem"
$Name = "LongPathsEnabled"
$Value = 1

if (Test-Path $RegistryPath) {
    Set-ItemProperty -Path $RegistryPath -Name $Name -Value $Value
    Write-Host "✅ Long Path support has been enabled." -ForegroundColor Green
    Write-Host "Please restart your computer or restart your shell for changes to take effect." -ForegroundColor Cyan
} else {
    Write-Error "Could not find registry path: $RegistryPath"
}
