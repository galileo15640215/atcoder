l = list(saikyo_holi_df['station_name'])
lon = list(saikyo_holi_df['lon'])
lat = list(saikyo_holi_df['lat'])
station_cd = list(saikyo_holi_df['station_cd'])
for i in range(len(l)):
  if l[i] == '日進':
    lon[i] = 139.606111
    lat[i] = 35.931555
    station_cd[i] = 1132120
  elif l[i] == '東雲':
    lon[i] = 139.804395
    lat[i] = 35.640987
    station_cd[i] = 9933702
saikyo_holi_df['lon'] = lon
saikyo_holi_df['lat'] = lat
saikyo_holi_df['station_cd'] = station_cd
