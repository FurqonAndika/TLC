import QtQuick 2.14
import QtQuick.Window 2.14
import QtQuick.Controls 1.6
import QtQuick.Extras 1.4
import Qt.labs.calendar 1.0

Window {
    id: window
    visible: true
    width: 640
    height: 480
    color: "#202d3d"
    title: qsTr("Meter Combination")
    flags: Qt.Window | Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint

    Image {
        id: image
        x: 0
        y: 0
        width: 640
        height: 485
        fillMode: Image.PreserveAspectFit
        source: "asset/Car-Dashboard-2-main/assets/Dashboard.svg"

        Image {
            id: image1
            x: 79
            y: 26
            width: 467
            height: 182
            fillMode: Image.PreserveAspectFit
            source: "asset/Car-Dashboard-2-main/assets/Vector 70.svg"

            Image {
                id: image2
                x: 157
                y: 235
                width: 100
                height: 141
                fillMode: Image.PreserveAspectFit
                source: "asset/Car-Dashboard-2-main/assets/Vector 1.svg"
            }

            Image {
                id: image4
                x: 217
                y: 284
                width: 74
                height: 60
                fillMode: Image.PreserveAspectFit
                source: "asset/Car-Dashboard-2-main/assets/car.png"
            }

            Image {
                id: image6
                x: 142
                y: 131
                width: 41
                height: 43
                fillMode: Image.PreserveAspectFit
                source: "asset/Car-Dashboard-2-main/assets/thirdRightIcon_red.svg"
                objectName: "parkingBrake"



            }
            Image {
                id: image5
                x: 276
                y: 125
                width: 49
                height: 55
                fillMode: Image.PreserveAspectFit
                source: "asset/Car-Dashboard-2-main/assets/Parking lights.svg"
                objectName: "headLamp"
            }
        }

        Image {
            id: image3
            x: 331
            y: 249
            width: 100
            height: 150
            fillMode: Image.PreserveAspectFit
            source: "asset/Car-Dashboard-2-main/assets/Vector 2.svg"
        }
    }

    Text {
        id: element
        x: 102
        y: 261
        width: 32
        height: 52
        color: "#d6cbcb"
        text: qsTr("0")
        horizontalAlignment: Text.AlignHCenter
        font.pixelSize: 40
        objectName: "text"
    }

    ToggleButton {
        id: toggleButton
        x: 55
        y: 420
        width: 49
        height: 38
        text: qsTr("Button")
        objectName: "button_1"
    }



    CircularGauge {
        id: circularGauge
        x: 428
        y: 148
        width: 190
        height: 190
        minimumValue: 0
        stepSize: 0
        maximumValue: 150
        value: 0
        objectName: "kecepatan"
    }

    Text {
        id: element1
        x: 165
        y: 80
        color: "#f7f2f8"
        text: qsTr("Tanggal")
        font.pixelSize: 18
        objectName: "Tanggal"
    }

    Text {
        id: element2
        x: 438
        y: 80
        color: "#efebe9"
        text: qsTr("Jam")
        font.pixelSize: 18
        objectName: "Jam"
    }

    CircularGauge {
        id: circularGauge1
        x: 23
        y: 148
        width: 190
        height: 190
    }

    Text {
        id: element4
        x: 81
        y: 310
        width: 75
        height: 28
        color: "#d6cbcb"
        text: qsTr("RPM")
        font.pixelSize: 20
        objectName: "text"
        horizontalAlignment: Text.AlignHCenter
    }

    Text {
        id: element3
        x: 507
        y: 261
        width: 32
        height: 52
        color: "#d6cbcb"
        text: qsTr("0")
        font.pixelSize: 40
        objectName: "text_kecepatan"
        horizontalAlignment: Text.AlignHCenter
    }




}


