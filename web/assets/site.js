document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{
 const platform=button.dataset.filter;
 document.querySelectorAll('[data-filter]').forEach(item=>item.setAttribute('aria-pressed',String(item===button)));
 document.querySelectorAll('[data-platforms]').forEach(item=>item.hidden=platform!=='all'&&!item.dataset.platforms.split(' ').includes(platform));
}));
const copy=document.querySelector('[data-copy]');
if(copy)copy.addEventListener('click',async()=>{
 const node=document.getElementById('page-address');
 try{await navigator.clipboard.writeText(node.textContent.trim());copy.textContent=copy.dataset.ok}
 catch{node.hidden=false;const s=getSelection();const r=document.createRange();r.selectNodeContents(node);s.removeAllRanges();s.addRange(r);copy.textContent=copy.dataset.selected}
});

function openLinkedDevice() {
 const id=location.hash.slice(1);
 const target=document.getElementById(id);
 for (const link of document.querySelectorAll('.device-links a')) {
   if (link.hash === location.hash) link.setAttribute('aria-current','location');
   else link.removeAttribute('aria-current');
 }
 if (!target) return;
 let parent=target;
 while(parent){if(parent.tagName==='DETAILS')parent.open=true;parent=parent.parentElement;}
 if(target.closest('.technical'))requestAnimationFrame(()=>target.scrollIntoView());
 for (const link of document.querySelectorAll('.langs a')) {
   const next=new URL(link.href);
   next.hash=id;
   link.href=next.href;
 }
}
window.addEventListener('hashchange',openLinkedDevice);
document.querySelectorAll('.device-links a').forEach(link=>link.addEventListener('click',()=>{
 const target=document.getElementById(link.hash.slice(1));
 if(target)target.open=true;
}));
openLinkedDevice();
