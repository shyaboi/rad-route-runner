if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) { Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs; exit }

Write-Output "111111111111111111111111111111111111111111111111111"

$url = "https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe"
$output = "$PSScriptRoot\py.exe"
$start_time = Get-Date

Import-Module BitsTransfer
Start-BitsTransfer -Source $url -Destination $output
#OR
Start-BitsTransfer -Source $url -Destination $output -Asynchronous

Write-Output "Time taken: $((Get-Date).Subtract($start_time).Seconds) second(s)"

msiexec /i "$PSScriptRoot\py.exe" /qn /norestart | Out-Null

Write-Output "installed py"

Read-Host -Prompt "Press Enter to exit"