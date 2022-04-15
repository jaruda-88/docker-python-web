let api = {
    type: "server",

    get url()
    {
        switch(this.type)
        {
            case "server":
                return 'http://3.38.135.214:5040/api';
            case "local":
                return 'http://192.168.1.69:5040/api';
            case "develop":
                return 'http://localhost:5040/api';
            default:
                return '';
        }
    }
};


function DeleteToken()
{
    sessionStorage.removeItem('token');    
};

function CommonErros(xhr, exception)
{
    console.log("error_status : " + xhr.status);
    console.log("error_Msg : " + xhr.responseText);
    var err = JSON.parse(xhr.responseText);
    console.log("error_resultCode : " + err['resultCode'])
    alert(err['resultMsg']);
    if(code == 406 || code == 401)
    {
        DeleteToken();
    }
};

