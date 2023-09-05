import js2py

#code_2 = "function f(x) {return x+x;}"
code_2 = """load("https://cdn.jibestream.com/web/plugins/geofencekit/v1.0.0/geofencekit.js");
 load("https://cdnjs.cloudflare.com/ajax/libs/gsap/1.19.0/easing/EasePack.min.js");
 load("https://cdn.jibestream.com/web/4.7.4/jmap.min.js");"""
res_2 = js2py.eval_js(code_2)


#print(res_2(5))
