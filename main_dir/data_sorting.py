import pymysql
from shapely.geometry.polygon import Polygon
import pandas as pd
# data_list = ['1','2','3','4','5','6','7']?


# 20205021730
# 20205021830


def sorting(data_list):
    db_adress = pymysql.connect(
    user='root',
    passwd='1234',
    host='127.0.0.1',
    db='mqtt_db',
    charset='utf8'
    )
    
    new_start = data_list[0];
    new_end = data_list[1];
    new_lat1 = float(data_list[3]);
    new_long1 = float(data_list[4]);
    new_lat2 = float(data_list[5]);
    new_long2 = float(data_list[6]);
    new_lat3 = float(data_list[7]);
    new_long3 = float(data_list[8]);
    #print(new_start);
    #print(type(new_start));
    cursor = db_adress.cursor(pymysql.cursors.DictCursor)

    sql = "SELECT EXISTS(SELECT * FROM saved_data where %s < end AND %s > start) AS isCHK"
    cursor.execute(sql, (new_start, new_end))
    result = cursor.fetchall()
    print(result[0]['isCHK']);
    print(type(result[0]['isCHK']));

    if result[0]['isCHK'] == 0:
        sql = "INSERT INTO saved_data (start, end, code, lat1, long1,lat2,long2,lat3,long3) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        new_start = int(data_list[0]);
        new_end = int(data_list[1]);
        cursor.execute(sql, (new_start, new_end, data_list[2], float(data_list[3]),float(data_list[4]),float(data_list[5]),float(data_list[6]),float(data_list[7]),float(data_list[8])))
        db_adress.commit();
        print(" 겹치는 시간대가 없음 > 추가성공")
        return " 겹치는 시간대가 없음 > 추가성공"
    else:
        print("겹치는 시간대가 있음");
        sql = "SELECT * FROM saved_data where %s < end AND %s > start"
        cursor.execute(sql,(new_start, new_end))
        result = cursor.fetchall()
        result1 = pd.DataFrame(result).loc[:,['lat1','long1']];
        result_np1 = pd.DataFrame.to_numpy(result1);
        result2 = pd.DataFrame(result).loc[:,['lat2','long2']];
        result_np2 = pd.DataFrame.to_numpy(result2);
        result3 = pd.DataFrame(result).loc[:,['lat3','long3']];
        result_np3 = pd.DataFrame.to_numpy(result3);
        flag = 0
        i = 0
        for t in result:
            if Polygon([(new_lat1, new_long1),(new_lat2,new_long2),(new_lat3,new_long3)]).intersects(Polygon([result_np1[i],result_np2[i],result_np3[i]])):
                flag = 1;
                break;
            else: i = i + 1

        if flag == 1:
            print("겹치는 시간대가 있음 > 겹치는 범위가 있음 > 추가 실패")
            return "겹치는 시간대가 있음 > 겹치는 범위가 있음 > 추가 실패"
        else:
            sql = "INSERT INTO saved_data (start, end, code, lat1, long1,lat2,long2,lat3,long3) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            new_start = int(data_list[0]);
            new_end = int(data_list[1]);
            cursor.execute(sql, (new_start, new_end, data_list[2], float(data_list[3]),float(data_list[4]),float(data_list[5]),float(data_list[6]),float(data_list[7]),float(data_list[8])))
            db_adress.commit();
            print("겹치는 시간대가 있음 > 겹치는 범위가 없음 > 추가 성공")
            return "겹치는 시간대가 있음 > 겹치는 범위가 없음 > 추가 성공"
