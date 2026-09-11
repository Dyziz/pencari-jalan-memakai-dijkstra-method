# Pencari Jalan Memakai Metode Dijkstra 🗺️

Yap, jadi ini ceritanya gw lagi iseng bikin project buat nyari rute/jalan terpendek. Yapping dikit ya.

## Latar Belakang

Awalnya gw ambil data map dari **OSMnx** (OpenStreetMap + NetworkX). Jadi gw download data jalan dari OpenStreetMap, terus di-convert jadi graph pakai OSMnx biar bisa diproses pakai NetworkX.

Terus gw mau nentuin **koordinat awal dan tujuan**. Rencananya sih awal dari **UNEJ** (Universitas Jember). Tapi... karena gk ketemu (mungkin di OSM gk ada node-nya, atau naming-nya beda), akhirnya gw pakai **koordinat manual** aja. Contohnya kayak rute **UNEJ ke Polije** gitu, pakai latitude/longitude langsung.

## Metode: Dijkstra

Buat nyari jalurnya, gw pakai **algoritma Dijkstra** — algoritma klasik buat nyari shortest path di graph berbobot.

Setelah dapet route-nya (list of nodes), gw hitung total jaraknya manual pakai snippet ini:

```python
total_dist = 0
for u, v in zip(route[:-1], route[1:]):
    edge_data = G[u][v]
    # Ambil yang paling pendek / pakai metode BFS yang disediakan
    min_length = min(d.get('length', 0) for d in edge_data.values())
    total_dist += min_length
```

btw readme yg bikin ai krn gw males yapping panjang2 asli, sama sebenarnya ada metode looping bfs berbobot cuma gw disarankan pake template
so yeah lol, cya.
