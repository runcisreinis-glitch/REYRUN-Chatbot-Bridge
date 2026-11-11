document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{
 const platform=button.dataset.filter;
 document.querySelectorAll('[data-filter]').forEach(item=>item.setAttribute('aria-pressed',String(item===button)));
 document.querySelectorAll('[data-platforms]').forEach(item=>item.hidden=platform!=='all'&&!item.dataset.platforms.split(' ').includes(platform));
}));
const copy=document.querySelector('[data-copy]');
if(copy)copy.addEventListener('click',async()=>{
 const node=document.getElementById('prompt');
 try{await navigator.clipboard.writeText(node.textContent.trim());copy.textContent=copy.dataset.ok}
 catch{const s=getSelection();const r=document.createRange();r.selectNodeContents(node);s.removeAllRanges();s.addRange(r);copy.textContent=copy.dataset.selected}
});
const launch=document.getElementById('first-launch');
const browserStart=document.getElementById('browser-start');
if(launch&&browserStart){
 const ua=navigator.userAgent;
 const mobile=/Android|iPhone|iPad|iPod/.test(ua)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
 if(mobile){
   const options=launch.parentElement.querySelector('p.small');
   const desktop=Array.from(launch.children);
   launch.prepend(browserStart);
   browserStart.className='btn primary';
   for(const link of desktop){link.className='';options.append(link,document.createTextNode('  '));}
 }else if(/Mac/.test(navigator.platform)){
   const mac=launch.lastElementChild,win=launch.firstElementChild;
   launch.prepend(mac);mac.classList.add('primary');win.classList.remove('primary');
 }
}
