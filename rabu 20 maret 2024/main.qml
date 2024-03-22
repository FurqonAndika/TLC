import QtQuick 2.14
import QtQuick.Window 2.14
import QtQuick.Controls 2.13
import QtQuick.Extras 1.4


Window {
    visible: true
    width: 640
    height: 480
    color: "#111512"
    title: qsTr("Aplikasi QT TLC")
    flags: Qt.Window | Qt.WindowMinimizeButtonHint //| Qt.WindowCloseButtonHint

    Image {
        id: image1
        x: 0
        y: 35
        width: 640
        height: 395
        source: "asset/Dashboard.svg"
        fillMode: Image.PreserveAspectFit

        Image {
            id: image2
            x: 59
            y: -25
            width: 522
            height: 206
            source: "asset/Vector 70.svg"
            fillMode: Image.PreserveAspectFit

            Image {
                id: image6
                x: 231
                y: 117
                width: 60
                height: 53
                source: "asset/hazard.png"
                fillMode: Image.PreserveAspectFit
            }

            ToggleButton {
                id: toggleButton
                x: 91
                y: 321
                width: 48
                height: 45
                text: qsTr("Button")

                ColorAnimation {
                    from: "white"
                    to: "black"
                    duration: 200
                }
            }
        }
    }
    Text {
        id: element
        x: 165
        y: 237
        color: "#eedede"
        text: qsTr("0")
        font.family: "Digital-7"
        font.bold: true
        font.pixelSize: 33
        objectName: "text1"

    }



    CircularGauge {
        id: circularGauge
        x: 72
        y: 125
        width: 201
        height: 199
        stepSize: 0
        maximumValue: 50
        value: 0
        objectName: "rpm"

        Image {
            id: image3
            x: 151
            y: 169
            width: 100
            height: 100
            source: "asset/Vector 1.svg"
            fillMode: Image.PreserveAspectFit
        }

        Image {
            id: image4
            x: 258
            y: 169
            width: 100
            height: 100
            source: "asset/Vector 2.svg"
            fillMode: Image.PreserveAspectFit
        }

        Image {
            id: image5
            x: 225
            y: 181
            width: 63
            height: 77
            source: "asset/Car.svg"
            fillMode: Image.PreserveAspectFit
        }
    }

    Text {
        id: element1
        x: 411
        y: 76
        color: "#ffffff"
        text: qsTr("20-3-2024")
        font.pixelSize: 17
        objectName: "tanggal"
    }

    Text {
        id: element2
        x: 287
        y: 76
        color: "#ffffff"
        text: qsTr("14:02:20")
        horizontalAlignment: Text.AlignHCenter
        styleColor: "#3ada69"
        font.pixelSize: 17
        objectName: "jam"
    }
    Button {
        id: button
        x: 351
        y: 179
        text: qsTr("tombol")
        scale: 1.1
        flat: true
        autoRepeat: false
        visible: true
        objectName: "button1"



    }

    CircularGauge {
        id: circularGauge1
        x: 373
        y: 125
        width: 201
        height: 199
        maximumValue: 150
        value: 0
        stepSize: 0
        objectName: "rpm"

        TextInput {
            id: textInput
            x: -243
            y: 137
            width: 80
            height: 20
            color: "#fdfdfd"
            text: qsTr("RPM")
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: 12
        }

        Image {
            id: image
            x: 119
            y: 233
            width: 26
            height: 25
            source: "asset/FirstRightIcon_grey.svg"
            fillMode: Image.PreserveAspectFit
        }
    }

    Text {
        id: element3
        x: 466
        y: 237
        color: "#eedede"
        text: qsTr("0")
        font.pixelSize: 33
        font.family: "Digital-7"
        font.bold: true
        objectName: "text1"
    }



}
