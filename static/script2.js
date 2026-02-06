let navigation = document.querySelector('.navigation');
let toggle = document.querySelector('.toggle');
toggle.onclick = function(){
    navigation.classList.toggle('active')
}


window.addEventListener("DOMContentLoaded", () => {
    let navigation = document.querySelector('.navigation');
    let toggle = document.querySelector('.toggle');

    toggle.onclick = function(){
        navigation.classList.toggle('active')
    }

    let tl = gsap.timeline();

    // Logo animation
    tl.from(".logo", {
        y: -20,
        duration: 0.5,
        opacity: 0,
        ease: "power2.out",
        delay:0.5
    });

    // Navbar links animation with realistic stagger time (0.2s each)
    tl.from(".navbar a", {
        y:-20,
        opacity: 0,
        duration: 0.1,
        stagger: 0.2,
        ease: "power2.out",
        
    }, "-=0.1"); // starts just before logo animation ends

    // At the end, ensure all links are fully visible
    tl.to(".navbar a", {opacity: 1}, "-=0.1"); 
});