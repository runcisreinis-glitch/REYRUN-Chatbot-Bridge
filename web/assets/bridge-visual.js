(() => {
  'use strict';
  const canvas = document.getElementById('bridge-art');
  if (!canvas) return;
  const ctx = canvas.getContext('2d', { alpha: true });
  if (!ctx) return;

  const W = 680, H = 385, TAU = 2 * Math.PI;
  const still = window.matchMedia('(prefers-reduced-motion: reduce)');
  const aqua = '#79eadb', gold = '#e1ab72';
  let width = 1, height = 1, frame = 0, visible = true, previous = -Infinity;
  let pointer = 0, drift = 0;

  function path(points, color, weight = 1, fill) {
    ctx.beginPath();
    points.forEach(([x, y], i) => i ? ctx.lineTo(x, y) : ctx.moveTo(x, y));
    if (fill) { ctx.closePath(); ctx.fillStyle = fill; ctx.fill(); }
    if (color) { ctx.strokeStyle = color; ctx.lineWidth = weight; ctx.stroke(); }
  }
  function traced(shape, color, size = 1, fill) {
    if (fill) { ctx.fillStyle = fill; ctx.fill(shape); }
    ctx.lineWidth = size; ctx.strokeStyle = color; ctx.stroke(shape);
  }
  function dot(x, y, r, color) {
    ctx.fillStyle = color; ctx.beginPath(); ctx.arc(x, y, r, 0, TAU); ctx.fill();
  }
  function glow(x, y, radius, color) {
    const g = ctx.createRadialGradient(x, y, 0, x, y, radius);
    g.addColorStop(0, color); g.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.fillStyle = g; ctx.fillRect(x-radius, y-radius, radius*2, radius*2);
  }

  const outline = new Path2D('M-75 1 C-81 -10 -78 -24 -70 -33 C-68 -48 -56 -57 -43 -60 C-33 -73 -16 -75 -5 -73 C8 -79 22 -75 33 -71 C49 -72 61 -64 70 -55 C85 -49 93 -38 93 -24 C103 -11 100 3 91 13 C89 25 78 32 64 33 C56 41 41 42 28 37 C13 45 -4 39 -12 30 C-24 34 -39 28 -45 19 C-56 23 -70 15 -75 1Z');
  const folds = [
    'M-68 -24 C-50 -26 -62 -44 -47 -46 S-36 -57 -30 -62',
    'M-63 -6 C-60 -17 -48 -9 -45 -23 S-51 -31 -38 -39 S-31 -50 -22 -54',
    'M-49 7 C-45 -4 -34 2 -30 -10 S-35 -24 -20 -31 S-26 -40 -14 -47',
    'M-26 11 C-10 10 -14 -4 -4 -10 S6 -18 1 -27 S11 -43 6 -54 S12 -63 14 -69',
    'M-32 18 C-11 28 0 18 12 11 S25 5 31 8 C38 12 49 9 57 2',
    'M7 25 C17 32 30 24 40 23 S51 27 58 18 S70 12 79 10',
    'M22 1 C34 -9 19 -12 28 -24 S36 -32 31 -44 S40 -56 43 -59',
    'M44 -2 C51 -16 37 -19 45 -28 S54 -31 53 -41 S62 -44 65 -48',
    'M62 -2 C64 -13 59 -16 66 -22 S80 -26 78 -35',
    'M80 -3 C78 -12 91 -12 88 -23',
    'M-22 -64 C-15 -60 -6 -66 -1 -61',
    'M28 -62 C24 -58 22 -51 24 -47'
  ].map(d => new Path2D(d));
  const cerebellum = new Path2D('M48 32 C66 26 84 23 88 33 C92 46 75 60 58 57 C47 55 44 43 48 32Z');
  const stem = new Path2D('M37 32 C49 37 50 41 55 52 C59 61 59 67 68 76 L57 79 C46 70 40 63 39 54 C35 47 28 46 27 40Z');

  function brain(t) {
    ctx.save(); ctx.translate(101 - drift * 1.2, 157 + Math.sin(t*.38)*1.5); ctx.scale(.88,.88);
    glow(0,-10,113,'rgba(42,150,150,.16)');
    traced(stem,'#518f98',1.15,'#113245');
    path([[37,40],[44,52],[49,63],[60,75]],'#77aaa9',.8);
    traced(cerebellum,'#66b4b5',1.2,'#133344');
    ctx.save();ctx.clip(cerebellum);
    for (let j=0;j<8;j++) {
      const y=32+j*3.6;
      traced(new Path2D('M46 '+y+' Q73 '+(y+9)+' 90 '+(y-7)),'#74c5bb',.65);
    }
    ctx.restore();
    traced(outline,'#a3f4dc',1.8,'#0c2b3b');
    ctx.save();ctx.clip(outline);
    for (let j=-4;j<6;j++){
      const y=j*13;
      traced(new Path2D('M-77 '+y+' Q4 '+(y-37)+' 99 '+(y+11)),'rgba(122,216,205,.16)',.8);
    }
    for (let j=-5;j<7;j++){
      const x=j*17;
      traced(new Path2D('M'+x+' -80 Q'+(x-30)+' -10 '+(x+17)+' 42'),'rgba(132,222,213,.15)',.8);
    }
    for (const f of folds) {
      traced(f,'#0c283b',5);
      traced(f,'#67bfb7',1.35);
    }
    [[-45,-23],[-4,-10],[31,8],[57,2],[66,-22],[-22,-54],[24,-47]].forEach(([x,y],i)=>{
      dot(x,y,1.6,i%3 ? '#d7b890' : '#c9fff0');
    });
    ctx.restore();ctx.restore();
  }

  function monitor(t) {
    ctx.save(); ctx.translate(0, Math.sin(t*.38+1.5)*1.1);
    const outer=[[496,97],[627,117],[626,213],[496,192]];
    const screen=[[503,105],[619,122],[618,200],[503,182]];
    path([[560,196],[572,198],[571,220],[556,219]],'#5f8588',1,'#19404d');
    path([[540,218],[569,213],[592,220],[566,226]],'#8facaa',1,'#2e505a');
    path([[625,116],[633,112],[632,208],[626,213]],'#547b82',1,'#193a47');
    path([[496,97],[504,93],[633,112],[626,118]],'#97b9b5',1,'#37575c');
    path(outer,'#a2c8bb',1.4,'#263b46');path(screen,'#131d2f',1.4,'#071f30');
    function onScreen(u,v){return [503+116*u,105+17*u+77*v];}
    ctx.save(); ctx.beginPath(); screen.forEach(([x,y],i)=>i?ctx.lineTo(x,y):ctx.moveTo(x,y));ctx.closePath();ctx.clip();
    glow(553,153,64,'rgba(71,211,192,.24)');
    for(let i=1;i<8;i++)path([onScreen(i/8,0),onScreen(i/8,1)],'rgba(122,209,201,.15)',.6);
    for(let i=1;i<5;i++)path([onScreen(0,i/5),onScreen(1,i/5)],'rgba(122,209,201,.19)',.6);
    for(let i=0;i<3;i++){
      const pts=[];for(let k=0;k<=50;k++){const u=k/50;const wave=.5+(.12+.025*i)*Math.sin(u*TAU*1.7+t*.34+i*.55)*Math.sin(u*Math.PI);pts.push(onScreen(u,wave));}
      path(pts,i?'#427f89':'#78e4d2',i?.7:1.5);
    }
    ctx.restore();dot(612,206,1.15,aqua);ctx.restore();
  }

  // Near and far rail projections follow the same curved deck.
  function deck(u,near){
    const side=near ? 1 : 0;
    return [136+373*u-16*side,194+25*side+33*Math.sin(u*Math.PI)-10*u];
  }
  function top(u,near) {
    const at=deck(u,near); return [at[0],at[1]- (near?107:101)];
  }
  const t1=.28,t2=.72;
  function cable(u,near){
    let left=0,right=t1,depth=6;
    if(u>=t2){left=t2;right=1;depth=6;}
    else if(u>=t1){left=t1;right=t2;depth=53;}
    const a=left===0?deck(0,near):top(left,near);
    const b=right===1?deck(1,near):top(right,near);
    const q=(u-left)/(right-left);
    return [a[0]+q*(b[0]-a[0]),a[1]+q*(b[1]-a[1])+4*depth*q*(1-q)];
  }
  function rails(near){
    const bright=near?'#d5a071':'#887d69';
    for(let k=1;k<34;k++){
      const u=k/34;
      path([cable(u,near),deck(u,near)],near?'rgba(210,159,107,.62)':'rgba(133,148,139,.40)',near?.86:.68);
    }
    const line=[];for(let i=0;i<=100;i++)line.push(cable(i/100,near));
    path(line,'#423c3a',3.3);path(line,bright,near?1.55:1);
    for(const u of [t1,t2]){
      const a=top(u,near),b=deck(u,near);
      path([[a[0]-2,a[1]-3],[a[0]+2,a[1]-3],[b[0]+3,b[1]+12],[b[0]-3,b[1]+12]],bright,.9,near?'#745348':'#434b4c');
      dot(a[0],a[1]-3,2,'#edc290');
    }
  }
  function bridge(t){
    ctx.save();ctx.translate(drift,0);
    for(const u of [t1,t2]){
      const a=top(u,false),b=top(u,true);
      path([[a[0]-2,a[1]],[a[0]+2,a[1]+4],[b[0]+2,b[1]+4],[b[0]-2,b[1]]],'#ac8f74',.8,'#785f51');
      path([[b[0],b[1]+15],[a[0],a[1]+24]],'#99795f',1.2);
    }
    rails(false);
    const far=[],near=[];for(let i=0;i<=70;i++){far.push(deck(i/70,false));near.push(deck(i/70,true));}
    path([...far,...near.slice().reverse()],'#769392',1,'#153646');
    for(let i=0;i<=28;i++){
      const u=i/28, p=deck(u,true);path([deck(u,false),p],'#4e7880',.65);
      if(i<28){const b=deck((i+1)/28,true);path([p,[b[0],b[1]+6]],'#b38261',.8);}
    }
    path(near.map(p=>[p[0],p[1]+6]),'#af805e',1.2);path(near,'#f0bb87',1.55);path(far,'#70bcad',1.05);
    ctx.font='7px monospace';ctx.textAlign='center';
    for(let lane=0;lane<2;lane++){
      for(let k=0;k<25;k++){
        const u=(k/25+t*.021+lane*.016)%1;
        const a=deck(u,false),b=deck(u,true),v=lane?.67:.33;
        const x=a[0]+(b[0]-a[0])*v,y=a[1]+(b[1]-a[1])*v;
        ctx.fillStyle=k%5===0?'#9fffe5':'#68abaf';ctx.fillText(k%3?'1':'0',x,y);
        if(k%8===0)glow(x,y-2,5,'rgba(102,232,209,.50)');
      }
    }
    rails(true);ctx.restore();
  }
  function render(t) {
    const ratio=Math.min(width/W,height/H);
    ctx.setTransform(canvas.width/width,0,0,canvas.height/height,0,0);
    ctx.clearRect(0,0,width,height);
    ctx.translate((width-W*ratio)/2,(height-H*ratio)/2);ctx.scale(ratio,ratio);
    ctx.lineCap='round';ctx.lineJoin='round';
    glow(322,206,154,'rgba(37,94,107,.17)');
    glow(207,174,104,'rgba(144,94,49,.12)');
    for(let i=0;i<39;i++){
      const x=22+(i*139)%634,y=61+(i*73)%230;
      dot(x,y,i%5===0?.9:.55,i%4===0?'#638285':'#3b5868');
    }
    path([[29,283],[215,254],[447,296],[644,255]],'rgba(70,111,124,.18)',.75);
    brain(t);monitor(t);bridge(t);
  }
  function draw(now){
    if (!visible) return;
    if(now-previous>40||still.matches){ drift+=(pointer-drift)*.045;render(still.matches?0:now/1000);previous=now;}
    if(!still.matches) frame=requestAnimationFrame(draw);
  }
  function refresh(){
    cancelAnimationFrame(frame);previous=-Infinity;
    const rect=canvas.getBoundingClientRect();
    width=Math.max(1,rect.width);height=Math.max(1,rect.height);
    const dpr=Math.min(window.devicePixelRatio||1,2);
    canvas.width=Math.round(width*dpr);canvas.height=Math.round(height*dpr);
    if(visible)frame=requestAnimationFrame(draw);
  }
  if('ResizeObserver' in window) new ResizeObserver(refresh).observe(canvas);
  else window.addEventListener('resize',refresh,{passive:true});
  canvas.addEventListener('pointermove',e=>{
    const bounds=canvas.getBoundingClientRect();pointer=still.matches?0:((e.clientX-bounds.left)/width-.5)*3;
  },{passive:true});
  canvas.addEventListener('pointerleave',()=>{pointer=0;},{passive:true});
  still.addEventListener('change',refresh);
  if('IntersectionObserver' in window) new IntersectionObserver(entries=>{
    visible=entries[0].isIntersecting;refresh();
  }).observe(canvas);
  refresh();
})();
