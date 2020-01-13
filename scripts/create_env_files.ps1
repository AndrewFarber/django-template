New-Item -ItemType Directory -Force -Path "..\src\env"

$django = "..\src\env" | Resolve-Path | Join-Path -ChildPath ".django"
$postgres = "..\src\env" | Resolve-Path | Join-Path -ChildPath ".postgres"
$db_pw = -join ((48..57) + (97..122) | Get-Random -Count 30 | % {[char]$_})
$secret_key = -join ((48..57) + (97..122) | Get-Random -Count 30 | % {[char]$_})

# Prompts
echo "`n"
$db_name = Read-Host "Database Name"
$db_user = Read-Host "Database User"

# Display 
echo "`nCreating .django config file"
echo "============================"
$env_file = "SECRET_KEY=$secret_key"
echo $env_file

# Export
[System.IO.File]::WriteAllLines($django, $env_file)


# Display 
echo "`nCreating .postgres config file"
echo "=============================="
$env_file = "POSTGRES_DB=$db_name"
$env_file = $env_file + "`n" + "POSTGRES_USER=$db_user"
$env_file = $env_file + "`n" + "POSTGRES_PASSWORD=$db_pw"
$env_file = $env_file + "`n" + "POSTGRES_HOST=db"
$env_file = $env_file + "`n" + "POSTGRES_PORT=5432"
echo $env_file

# Export
[System.IO.File]::WriteAllLines($postgres, $env_file)
echo "`n"