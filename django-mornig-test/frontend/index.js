console.log('hi')


window.onload = () => {
    const payload = localStorage.getItem("payload");
    console.log(JSON.parse(payload).email)

    const intro = document.getElementById("intro")
    intro.innerText = JSON.parse(payload).email
}