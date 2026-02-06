// Start state - invisible and small
gsap.set("h2, .container", { opacity: 0, scale: 0.8 });

// Sab headings + notices ko ek saath zoom-in
gsap.to("h2, .container", {
  opacity: 1,
  scale: 1,
  duration: 0.6,
  ease: "power2.out",
  delay: 0.3
});