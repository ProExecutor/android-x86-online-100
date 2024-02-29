from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
<!DOCTYPE HTML>
<html>
<head>
  <style>
    .center {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
  </style>
  <script src="{{ url_for('static', filename='jsvm.js') }}"></script>
  <script>
    javascript:(function () {     
      var script =  document.createElement('script');    
      script.src="//cdn.jsdelivr.net/npm/eruda";     
      document.body.appendChild(script);    
      script.onload = function () {         
        eruda.init()     
      } 
    })();
  </script>
</head>
<body>
  <vm-instance id="vm" class="center"></vm-instance>
  <script>
    document.getElementById('vm').setAttribute('cd-rom', 'cdrom/android-x86-1.6-r2.iso');
  </script>
</body>
</html>
    """)

if __name__ == '__main__':
    app.run(debug=True)
