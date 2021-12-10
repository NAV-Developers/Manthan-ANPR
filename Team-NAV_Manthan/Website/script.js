const plates = ["DL 33 AY 6324","HR 55 W 4347","DL 12 SD 7561","HR 51 AA 1997","DL 1 LF 7843"];
const details = [
    ["Adyar","Blue","Bajaj","Discover","None","Private","CAM-TN-112","Bike","https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31099.627260889847!2d80.24177583843914!3d13.00677327805422!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a5267ed15c41681%3A0x6569ce967a249e83!2sAdyar%2C%20Chennai%2C%20Tamil%20Nadu!5e0!3m2!1sen!2sin!4v1639077023789!5m2!1sen!2sin"],
    ["Medavakkam","White","Mahindra","Supro","None","Commercial","CAM-TN-0504","Mini Truck","https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31110.472684261716!2d80.16925083838892!3d12.919988796281102!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a525c1c2ab10c01%3A0x8f33fe8bebe2b89c!2sMedavakkam%2C%20Chennai%2C%20Tamil%20Nadu!5e0!3m2!1sen!2sin!4v1639076879426!5m2!1sen!2sin"],
    ["Velachery","Black","Hero","Platina","Insurance","Private","CAM-TN-0513","Bike","https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31103.086431100022!2d80.20070853842313!3d12.979155133864534!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a525d9ff2065a3b%3A0x66435015604038cc!2sVelachery%2C%20Chennai%2C%20Tamil%20Nadu!5e0!3m2!1sen!2sin!4v1639076942659!5m2!1sen!2sin"],
    ["Medavakkam","Black","Hero","Splendor","None","Private","CAM-TN-0514","Bike","https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31110.472684261716!2d80.16925083838892!3d12.919988796281102!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a525c1c2ab10c01%3A0x8f33fe8bebe2b89c!2sMedavakkam%2C%20Chennai%2C%20Tamil%20Nadu!5e0!3m2!1sen!2sin!4v1639076879426!5m2!1sen!2sin"],
    ["Sholinganallur","Green","Mahindra","Alfa Plus","None","Commercial","CAM-TN-0405","Mini Truck","https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31113.345040921085!2d80.20725856963185!3d12.896908217904418!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a525b79de7f381b%3A0xffbb2dd48afe3f1b!2sSholinganallur%2C%20Chennai%2C%20Tamil%20Nadu!5e0!3m2!1sen!2sin!4v1638864580816!5m2!1sen!2sin"]
];
function getIndex(str){
    var i=0;
    while(i < plates.length){
        if(plates[i] == str)
            return i;
        i++;
    }
    return -1;
}
function set(i){    
        document.getElementById("plate-no").innerHTML=plates[i];
        document.getElementById("location").innerHTML=details[i][0];
        document.getElementById("color").innerHTML=details[i][1];;
        document.getElementById("manufacturer").innerHTML=details[i][2];;
        document.getElementById("model").innerHTML=details[i][3];;
        document.getElementById("violations").innerHTML=details[i][4];;
        document.getElementById("type").innerHTML=details[i][5];;
        document.getElementById("ls").innerHTML=details[i][6];;
        document.getElementById("btype").innerHTML=details[i][7];;    
        document.getElementById("mapset").setAttribute("src",details[i][8]);
        var url = "Asset/"+(i+1)+".png";
        console.log(url);
        document.getElementById("vehicle-snap").setAttribute("src",url);

}

function highlight(ele){
    var m = document.getElementById("selected");
    if(m != null){
        m.removeAttribute("id");
        m.removeAttribute("style");
    }
    ele.setAttribute("id","selected");
    ele.setAttribute("style","background-color: #FF0000;color: white;");
    var x=ele.firstChild.nextSibling;
    var y=ele.lastChild.previousSibling;
    console.log(x.innerText +" "+y.innerText);
    set(getIndex(x.innerText));
}