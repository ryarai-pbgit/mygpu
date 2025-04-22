import pyarrow as pa
import pyarrow.flight
import pandas as pd

class CSVFlightServer(pyarrow.flight.FlightServerBase):
    def __init__(self, location):
        super().__init__(location)
        self.data = None
        self._location = location  # サーバーのアドレスを保存

    def set_data(self, data):
        self.data = data

    def get_flight_info(self, context, descriptor):
        if self.data is None:
            raise KeyError("No data available")
        schema = self.data.schema
        endpoints = [pyarrow.flight.FlightEndpoint("ticket-1", [self._location])]
        return pyarrow.flight.FlightInfo(
            schema,
            descriptor,
            endpoints,
            self.data.num_rows,
            self.data.nbytes
        )

    def do_get(self, context, ticket):
        if ticket.ticket.decode("utf-8") != "ticket-1":
            raise KeyError(f"Unknown ticket: {ticket.ticket}")
        return pyarrow.flight.RecordBatchStream(self.data)

if __name__ == "__main__":
    # CSVファイルを読み込む
    csv_file = "test_row_500.csv"  # 読み込むCSVファイルのパス
    df = pd.read_csv(csv_file)
    table = pa.Table.from_pandas(df)

    # サーバーを起動
    server = CSVFlightServer("grpc://0.0.0.0:8815")
    server.set_data(table)
    print("Flight server is running on grpc://0.0.0.0:8815")
    server.serve()
