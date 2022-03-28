let api = {
    type: "server",

    get url()
    {
        switch(type)
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