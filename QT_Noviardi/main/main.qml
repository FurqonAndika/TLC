import QtQuick 2.14
import QtQuick.Window 2.14

Window {
    visible: true
    width: 640
    height: 480
    color: "#b5c4d7"
    title: qsTr("Hello World")

    Text {
        id: element
        x: 31
        y: 24
        text: qsTr("TOYOTA")
        font.family: "Arial"
        horizontalAlignment: Text.AlignHCenter
        font.pixelSize: 12
    }
}
