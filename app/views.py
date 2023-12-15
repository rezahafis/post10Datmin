from app import app, render_template, request

@app.route("/")
def index():
  return render_template('utama.html')

@app.route('/datadiri', methods=['POST'])
def dataDiri():

  nim = int(request.form['nim'])
  nama = str(request.form['nama'])
  prodi = str(request.form['prodi'])

  hasilnim = nim
  hasilnama = nama
  hasilprodi = prodi

  return render_template('utama.html', hasilnim=hasilnim, hasilnama=hasilnama, hasilprodi=hasilprodi, nim=nim, nama=nama, prodi=prodi)


@app.route('/hitung', methods=['POST'])
def hitung():

  bil1 = int(request.form['bil1'])
  bil2 = int(request.form['bil2'])
    
  # ======================================================  

  hasil = bil1 + bil2
  hasil2 = bil1 - bil2
  hasil3 = bil1 * bil2
  hasil4 = bil1 / bil2
    
  return render_template('utama.html', hasil=hasil, hasil2=hasil2, hasil3=hasil3, hasil4=hasil4,bil1=bil1, bil2=bil2)


if __name__ == '__main__':
  app.run(debug=True)