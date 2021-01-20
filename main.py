import sys

from dotenv import load_dotenv

from assets import Asset, TimeFrame


def main():
    if '--paper' in sys.argv:
        load_dotenv('env/paper.env')

    if '--live' in sys.argv:
        load_dotenv('env/live.env')

    asset = Asset('TSLA')
    chart = asset.get_chart(TimeFrame.DAILY)

    print('TSLA')
    print(f'Change: {chart.last_percent_change:.2%}')
    print(f'Last bar is green: {chart.bars[-1].is_green}')


if __name__ == '__main__':
    main()
