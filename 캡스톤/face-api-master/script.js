const video = document.getElementById('video'); // take the video element from html

Promise.all([                                   //promise.all to call these asyncronous calls in parallel which is easy to execute.
    faceapi.nets.tinyFaceDetector.loadFromUri('./models'),
    faceapi.nets.faceLandmark68Net.loadFromUri('./models'), //different parts of faces = mouth,nose ,eyes
    faceapi.nets.faceRecognitionNet.loadFromUri('./models'),  //where is the face 
    faceapi.nets.faceExpressionNet.loadFromUri('./models'), //happy ,sad etc
]).then(startVideo)

function startVideo() {
    navigator.getUserMedia = (
        navigator.getUserMedia ||
        navigator.webkitGetUserMedia ||
        navigator.mozGetUserMedia ||
        navigator.msGetUserMedia
    );
    //To connect the video element with web cam
    navigator.getUserMedia(
        { video :{} },
        stream => video.srcObject = stream,    //stream method =whats coming from our web cam 
        err => console.error(err)

    )
}

video.addEventListener('play',() => {
    //create a canvas for faceapi which will be showed on video element
    const canvas = faceapi.createCanvasFromMedia(video);
    document.body.append(canvas);       //to append the canvas inside body
    const displaySize ={width : video.width ,height : video.height} //size of canvas same as video element
    faceapi.matchDimensions(canvas , displaySize)
    setInterval(async () =>{
        
        //To detect all the faces.
        const detections = await faceapi.detectAllFaces(video , new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions();
        
        //Displaying our elements inside the canvas.
        const resizedDetections = faceapi.resizeResults(detections , displaySize);

        //To clear the canvas before draw
        canvas.getContext('2d').clearRect(0,0,canvas.width,canvas.height)

        // to draw detections on canvas.
        faceapi.draw.drawDetections(canvas,resizedDetections)

        //To draw the landmarks(eyes,nose,etc)
        faceapi.draw.drawFaceLandmarks(canvas,resizedDetections)

        //To draw the expressions 
        faceapi.draw.drawFaceExpressions(canvas,resizedDetections)

    },100)
})
