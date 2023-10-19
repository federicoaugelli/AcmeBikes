include "console.iol"

type Component:void {
    .component_id:int
}

interface AcmeDbInterface {
    RequestResponse: checkIsAssembleable(Component)(int)
}

outputPort AcmeDbService {
    Location: "socket://localhost:8000/"
    Protocol: http { .method = "get" }
    Interfaces: AcmeDbInterface
}

main
{
    request.component_id = 4532
    checkIsAssembleable@AcmeDbService(request)( response );
    println@Console( response )()
}