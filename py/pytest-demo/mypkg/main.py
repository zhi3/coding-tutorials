import app
import view


def main():
    obj1 = app.App(1)
    obj2 = view.View(2)
    print('result: {}, {}'.format(obj1.getV(), obj2.getV()))


if __name__ == "__main__":
    main()
