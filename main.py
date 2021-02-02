import sys

from dotenv import load_dotenv

from clients import AssetClient


def main():
    if '--paper' in sys.argv:
        load_dotenv('env/paper.env')
    elif '--live' in sys.argv:
        load_dotenv('env/live.env')

    asset_client = AssetClient()
    assets = asset_client.get_available_assets()
    charts = asset_client.get_charts(assets)
    charts.sort(key=lambda c: c.last_percent_change or 0)
    for chart in charts:
        print(str(chart))


if __name__ == '__main__':
    main()
