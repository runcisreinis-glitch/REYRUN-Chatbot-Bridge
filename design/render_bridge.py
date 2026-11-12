"""Render the miniature bridge used in the public guide. Run with Blender 4.x."""
import math
from pathlib import Path
import bpy
from mathutils import Vector
from math import pi
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
def metal(name, color, metallic, roughness, glow=0):
    m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF')
    for key,value in [('Base Color',(*color,1)),('Metallic',metallic),('Roughness',roughness),('Coat Weight',.32),('Coat Roughness',.12)]:
        p.inputs[key].default_value=value
    if glow:
        p.inputs['Emission Color'].default_value=(*color,1)
        p.inputs['Emission Strength'].default_value=glow
    return m
slate=metal('Deep indigo ceramic',(.014,.027,.085),.62,.24)
case=metal('Night blue alloy',(.04,.085,.21),.82,.24)
edge=metal('Satin titanium',(.33,.53,.79),.87,.20)
silver=metal('Diamond-cut rim',(.72,.82,.98),.9,.15)
glass=metal('Polished sapphire',(.025,.12,.53),.67,.16)
light=metal('Ice-blue light guide',(.13,.57,1),.25,.19,1.55)
gold=metal('Copper contacts',(.64,.34,.16),.78,.23)
screen=metal('Screen glass',(.007,.044,.13),.4,.13)
def finish(obj,mat):
    obj.data.materials.append(mat);return obj
def slab(name,xyz,dims,mat,r=.04):
    bpy.ops.mesh.primitive_cube_add(size=1,location=xyz);o=bpy.context.object;o.name=name;o.dimensions=dims
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if r:
        b=o.modifiers.new('Polished corner','BEVEL');b.width=min(r,min(dims)*.48);b.segments=4
        n=o.modifiers.new('Planar normals','WEIGHTED_NORMAL')
    return finish(o,mat)
def wire(name,pts,r,mat):
    c=bpy.data.curves.new(name,'CURVE');c.dimensions='3D';c.resolution_u=1;c.bevel_depth=r;c.bevel_resolution=3
    s=c.splines.new('POLY');s.points.add(len(pts)-1)
    for p,co in zip(s.points,pts):p.co=(*co,1)
    o=bpy.data.objects.new(name,c);scene.collection.objects.link(o);return finish(o,mat)
def rivet(x,y,z):
    bpy.ops.mesh.primitive_cylinder_add(vertices=16,radius=.048,depth=.025,location=(x,y,z))
    finish(bpy.context.object,silver);slab('Screw slot',(x,y,z+.014),(.052,.011,.003),slate,.001)
def label(text,loc,size,mat):
    c=bpy.data.curves.new('Chip lettering','FONT');c.body=text;c.align_x='CENTER';c.align_y='CENTER';c.size=size;c.extrude=.014;c.bevel_depth=.002
    o=bpy.data.objects.new('Etched '+text,c);scene.collection.objects.link(o);o.location=loc;finish(o,mat)
for x in (-3.58,3.58):
    slab('Dark ceramic foot',(x,0,.06),(3.08,2.85,.32),slate,.14)
    slab('Milled silver edge',(x,0,.23),(3.06,2.83,.095),edge)
    slab('Sapphire island',(x,0,.34),(2.98,2.73,.15),case,.065)
    slab('Glazed top',(x,0,.433),(2.84,2.58,.045),glass)
    for a in (-1.27,1.27):
        for b in (-1.11,1.11):rivet(x+a,b,.465)
    for j in range(5):
        sy=-1.13+j*.12
        wire('Copper signal trace',[(x-1.23,sy,.458),(x-.78,sy,.458),(x-.63,sy+.15,.458),(x+.99,sy+.15,.458)],.009,edge if j%2 else gold)
# Microprocessor, with four separate banks of visible pins and cut silver sidewalls.
cx=-3.70
for n in range(-5,6):
    for side in (-1,1):
        slab('Processor lead',(cx+n*.126,side*.83,.64),(.068,.41,.075),gold,.025)
        slab('Processor lead',(cx+side*.87,n*.125,.64),(.42,.065,.075),gold,.022)
slab('Processor submount',(cx,0,.62),(1.8,1.7,.23),slate,.1)
slab('Processor rim',(cx,0,.79),(1.73,1.63,.14),silver,.06)
slab('Processor glass die',(cx,0,.915),(1.56,1.46,.16),glass,.07)
slab('Microchip face',(cx,0,1.015),(1.38,1.28,.065),case,.03);label('AI',(cx,0,1.057),.61,silver)
# Two pairs of portal uprights, suspended deck, parallel catenaries.
slab('Bridge chassis',(0,0,.62),(4.63,1.26,.24),slate,.07)
slab('Machined deck',(0,0,.758),(4.65,1.27,.07),silver,.03)
slab('Glass bridge deck',(0,0,.824),(4.65,1.20,.09),glass,.035)
for y in (-.48,.48):wire('Light in deck',[(-2.3,y,.879),(2.3,y,.879)],.018,light)
for x in [-1.99+i*.23 for i in range(18)]:wire('Deck inlay',[(x,-.38,.873),(x,.38,.873)],.009,edge)
for tx in (-1.39,1.39):
    for side in (-1,1):
        y=side*.665
        slab('Tower footing',(tx,y,.72),(.30,.28,.49),case)
        wire('Tower column',[(tx,y,.81),(tx,y*.947,2.21)],.070,edge)
        wire('Tower inset',[(tx,y-side*.025,.98),(tx,y*.947-side*.025,2.11)],.015,light)
    wire('Portal beam',[(tx,-.627,2.2),(tx,.627,2.2)],.055,silver)
    wire('Portal brace',[(tx,-.61,1.92),(tx,.56,2.17)],.026,edge)
    wire('Portal brace',[(tx,.61,1.92),(tx,-.56,2.17)],.026,edge)
for side in (-1,1):
    y=side*.64
    for a,b,za,zb,sag in [(-2.35,-1.39,.88,2.21,.085),(-1.39,1.39,2.21,2.21,.76),(1.39,2.35,2.21,.88,.085)]:
        def cable(q):return (a+(b-a)*q,y,za+(zb-za)*q-4*sag*q*(1-q))
        wire('Suspension cable',[cable(i/64) for i in range(65)],.032,silver)
        count=11 if (b-a)>2 else 4
        for i in range(1,count):
            x,cy,z=cable(i/count);wire('Hanger',[(x,cy,.87),(x,cy,z)],.014,gold)
# Screen, subtly angled away from the vertical and with a reflective bevel.
cx=3.67
slab('Monitor foot',(cx,.18,.51),(1.18,.67,.10),edge)
slab('Monitor neck',(cx,.27,.91),(.26,.19,.76),case)
slab('Monitor case',(cx,.35,1.65),(2.09,.15,1.34),edge,.07)
slab('Display bezel',(cx,.258,1.65),(2.02,.085,1.27),slate,.04)
slab('Display face',(cx,.207,1.65),(1.82,.026,1.06),screen,.02)
for i in range(6):
    z=1.22+i*.16;wire('Display grid',[(cx-.86,.189,z),(cx+.86,.189,z)],.003,edge)
points=[(cx-.78+1.56*q/64,.179,1.58+.15*math.sin(q/12)+.11*math.sin(q/5)*math.sin(pi*q/64)) for q in range(65)]
wire('Signal pulse',points,.015,light)
# Phone at a separate angle and scale; it remains recognizable on a narrow screen.
phone=[]
for name,pos,dims,mat,r in [
    ('Phone rim',(2.65,-.71,1.12),(.59,.10,1.30),silver,.05),
    ('Phone bezel',(2.65,-.772,1.12),(.55,.049,1.26),slate,.024),
    ('Phone face',(2.65,-.802,1.12),(.475,.027,1.11),glass,.013),
    ('Phone speaker',(2.65,-.821,1.61),(.15,.01,.027),slate,.003),
    ('Phone control',(2.65,-.822,.635),(.16,.012,.022),light,.003)]:
    phone.append(slab(name,pos,dims,mat,r))
for i,width in enumerate([.31,.22,.29]):
    slab('Phone signal',(2.64,-.819,1.26-i*.09),(width,.014,.02),light,.004)
def area(name,loc,color,energy,size):
    bpy.ops.object.light_add(type='AREA',location=loc);o=bpy.context.object;o.name=name;o.data.energy=energy;o.data.shape='DISK';o.data.size=size;o.data.color=color
    o.rotation_euler=(Vector((0,0,.7))-o.location).to_track_quat('-Z','Y').to_euler()
area('Softbox',(0,-5,8),(.77,.86,1),2900,7);area('Sapphire rim',(-5,4,5),(.12,.34,1),3700,5)
area('Icy rim',(4,3,6),(.50,.86,1),2800,5);area('Warm specular edge',(-6,-2,3),(1,.68,.42),610,3)
world=bpy.data.worlds.new('Midnight studio');scene.world=world;world.use_nodes=True;world.node_tree.nodes['Background'].inputs[0].default_value=(.20,.245,.40,1);world.node_tree.nodes['Background'].inputs[1].default_value=.45
bpy.ops.object.camera_add(location=(5.2,-16.8,9));cam=bpy.context.object;target=Vector((0,0,1.03))
cam.rotation_euler=(target-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=11.5;scene.camera=cam
scene.render.engine='CYCLES';scene.cycles.samples=112;scene.cycles.use_denoising=False;scene.render.resolution_x=1120;scene.render.resolution_y=590;scene.render.resolution_percentage=100
scene.render.film_transparent=True;scene.render.image_settings.file_format='WEBP';scene.render.image_settings.quality=94;scene.render.image_settings.color_mode='RGBA'
scene.render.filepath=str(Path(__file__).resolve().parents[1]/'web/assets/bridge-model.webp')
bpy.ops.render.render(write_still=True)
