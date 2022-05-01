# Mapbox-Isochrone-Generator
基于 Mapbox's Isochrone API 绘制多个点位的等时圈，并保存为 Shapefile 文件。

## 使用方式
1. 注册 Mapbox 账号，获取您的 access token 。
2. 修改 `isochrone.py` 文件，在此填写您的 access token 。
  ```
  YOUR_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
  ```
3. 修改 `data.csv` 文件，填写各种参数。参数要求见 https://docs.mapbox.com/api/navigation/isochrone/ 。
