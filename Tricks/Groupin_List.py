a = range(100)
zip(*(iter(a),) * 5)
