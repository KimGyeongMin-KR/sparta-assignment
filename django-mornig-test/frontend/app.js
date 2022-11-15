window.onload = () => {
    console.log('로딩됨')
}


async function handleSignin(){
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value
    console.log(email.value)

    const response = await fetch('http://127.0.0.1:8000/user/signup/', {
        headers : {
            'content-type' : 'application/json',
        },
        method : 'POST',
        body : JSON.stringify({
            "email" : email,
            "password" : password
        })
    })

    console.log(response)
}

async function handleLogin(){
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value


    const response = await fetch('http://127.0.0.1:8000/api/token/', {
        headers : {
            'content-type' : 'application/json',
        },
        method : 'POST',
        body : JSON.stringify({
            "email" : email,
            "password" : password
        })
    })

    const response_json = await response.json()

    console.log(response_json["access"])

    localStorage.setItem('access', response_json.access)
    localStorage.setItem('refresh', response_json.refresh)


    // const base64Url = response_json.access.split('.')[1];
    // const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    // const jsonPayload = decodeURIComponent(atob(base64).split('').map(function (c) {
    //     return '%' + ('00' + c.charCodeAt(0).toString(16).slice(-2));
    // }).join(''));
    const base64Url = response_json.access.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    localStorage.setItem('payload', jsonPayload)


}


async function handleMork(){

    const response = await fetch('http://127.0.0.1:8000/user/mock/', {
        headers : {
            "Authorization" : "Bearer " + localStorage.getItem("access"),
        },
        method : 'GET',
    })

    console.log(response)
}


function logout(){


    localStorage.removeItem('access')
    localStorage.removeItem('payload')
    localStorage.removeItem('refresh')
}