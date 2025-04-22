import pyarrow.flight

if __name__ == "__main__":
    # サーバーに接続
    client = pyarrow.flight.FlightClient("grpc://[internal ip of grpc server]:8815")

    # サーバーからデータを取得
    flight_info = client.get_flight_info(pyarrow.flight.FlightDescriptor.for_path("data"))
    reader = client.do_get(flight_info.endpoints[0].ticket)
    table = reader.read_all()

    # データを表示
    print("Downloaded data:")
    print(table.to_pandas())
