var typed = new Typed (".multiple-text", {
    strings : ["Future Innovators","Tech Transformers","Rising Stars",
        "From Learners to Leaders"],
    typeSpeed:50,
    backSpeed:100,
    backDelay:500,
    loop:true
})

const images = ["g1.jpg","g2.jpg","g3.jpg","g4.jpg","g5.jpg"];
let index = 0;
setInterval(() => {
    document.getElementById(".dynamic-img").src = images[index];
    index = (index + 1) % images.length;
},3000)