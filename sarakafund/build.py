src=open('app.html',encoding='utf-8').read()
head='''<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#0F4A38">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon.svg">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px)}body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>
'''
open('index.html','w',encoding='utf-8').write(head+src+'\n</html>\n')
