from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/zakat-emas', methods=['POST'])
def zakat_emas():
    try:
        data = request.get_json()
        total_nilai_emas = float(data['total_nilai_emas'])  # Total nilai emas dalam Rupiah
        harga_emas_per_gram = float(data['harga_emas_per_gram'])  # Harga emas per gram dalam Rupiah

        nisab = 85 * harga_emas_per_gram

        if total_nilai_emas >= nisab:
            zakat = 0.025 * total_nilai_emas  
        else:
            zakat = 0  

       
        return jsonify({
            "total_nilai_emas": total_nilai_emas,
            "harga_emas_per_gram": harga_emas_per_gram,
            "nisab": nisab,
            "zakat": zakat,
            "keterangan": "Wajib zakat" if zakat > 0 else "Tidak wajib zakat"
        })

    except (ValueError, KeyError):
        return jsonify({"error": "Input tidak valid. Pastikan mengirim 'total_nilai_emas' dan 'harga_emas_per_gram'."}), 400

@app.route('/zakat-perdagangan', methods=['POST'])
def zakat_perdagangan():
    try:
        # comment: 
        data = request.get_json()
        modal = float(data['modal'])  # Total modal dalam Rupiah
        keuntungan = float(data['keuntungan']) 
        piutang = float(data['piutang'])
        hutang= float(data['hutang'])
        kerugian = float(data['kerugian'])
        harga_emas_per_gram = float(data['harga_emas_per_gram'])  # Harga emas per gram dalam Rupiah

        nisab = 85 * harga_emas_per_gram
        nilai = (modal + keuntungan + piutang) - (kerugian + hutang)

        if nilai >= nisab:
            zakat = 0.025 * nilai  
        else:
            zakat = 0 

        return jsonify({
            "total harta": nilai,
            "harga_emas_per_gram": harga_emas_per_gram,
            "nisab": nisab,
            "zakat": zakat,
            "keterangan": "Wajib zakat" if zakat > 0 else "Tidak wajib zakat"
        })
    except (ValueError, KeyError):
        return jsonify({"error": "Input tidak valid. Pastikan mengirim 'total_nilai_emas' dan 'harga_emas_per_gram'."}), 400
    # end try
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
