"""Build store-ready zips: dist/skulldrift-crazygames.zip + dist/skulldrift-poki.zip.
Injects the platform SDK adapter at the <!-- PLATFORM_SDK --> marker."""
import os, zipfile

CG = """<script src="https://sdk.crazygames.com/crazygames-sdk-v3.js"></script>
<script>
window.PSDK = (function(){
  let sdk = null;
  const ready = (async()=>{ try { await window.CrazyGames.SDK.init(); sdk = window.CrazyGames.SDK; } catch(e){} })();
  return {
    ready,
    loaded(){ try { sdk && sdk.game.loadingStop && sdk.game.loadingStop(); } catch(e){} },
    start(){ try { sdk && sdk.game.gameplayStart(); } catch(e){} },
    stop(){ try { sdk && sdk.game.gameplayStop(); } catch(e){} },
    midgame(){ return new Promise(res => { if (!sdk) return res();
      try { sdk.ad.requestAd('midgame', { adFinished: res, adError: res, adStarted(){ } }); }
      catch(e){ res(); } }); }
  };
})();
</script>"""

POKI = """<script src="https://game-cdn.poki.com/scripts/v2/poki-sdk.js"></script>
<script>
window.PSDK = (function(){
  const ready = (async()=>{ try { await PokiSDK.init(); } catch(e){} })();
  return {
    ready,
    loaded(){ try { PokiSDK.gameLoadingFinished(); } catch(e){} },
    start(){ try { PokiSDK.gameplayStart(); } catch(e){} },
    stop(){ try { PokiSDK.gameplayStop(); } catch(e){} },
    midgame(){ try { return PokiSDK.commercialBreak(()=>{}).catch(()=>{}); } catch(e){ return Promise.resolve(); } }
  };
})();
</script>"""

src = open('index.html', encoding='utf-8').read()
assert '<!-- PLATFORM_SDK -->' in src, 'marker missing'
os.makedirs('dist', exist_ok=True)

# Bundle the licensed SFX the game references (sounds/*.mp3). index.html falls back to
# synth audio if a clip is missing, but ship the real ones so store builds sound right.
def add_dir(z, folder):
    if not os.path.isdir(folder):
        return
    for root, _, files in os.walk(folder):
        for f in files:
            p = os.path.join(root, f)
            z.write(p, os.path.relpath(p, '.').replace('\\', '/'))

for name, snippet in (('crazygames', CG), ('poki', POKI)):
    html = src.replace('<!-- PLATFORM_SDK -->', snippet, 1)
    out = f'dist/skulldrift-{name}.zip'
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('index.html', html)
        add_dir(z, 'sounds')
    print(out, os.path.getsize(out), 'bytes')
