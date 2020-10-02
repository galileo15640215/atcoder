l = list(soubu_week_df['station_name'])
lon = list(soubu_week_df['lon'])
lat = list(soubu_week_df['lat'])
for i in range(len(l)):
  if l[i] == '大久保':
    lon[i] = 139.69732
    lat[i] = 35.700784
soubu_week_df['lon'] = lon
soubu_week_df['lat'] = lat

l = list(soubu_holi_df['station_name'])
lon = list(soubu_holi_df['lon'])
lat = list(soubu_holi_df['lat'])
for i in range(len(l)):
  if l[i] == '大久保':
    lon[i] = 139.69732
    lat[i] = 35.700784
soubu_holi_df['lon'] = lon
soubu_holi_df['lat'] = lat
