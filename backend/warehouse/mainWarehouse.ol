include "console.iol"
include "warehouseInterface.iol"
include "http.iol"

inputPort MainWarehouseService {
	Location: "socket://localhost:8005"
	Protocol: sodep
	Interfaces: warehouseInterface
}

interface AcmeBikeDatabaseInterface {
    RequestResponse: getComponents(int)(bool)
}

outputPort AcmeBikeDatabase {
    Location: "socket://localhost:8004/checkIsAssembleable/{component_id}"
    Protocol: http { .method = "get" }
    Interfaces: AcmeBikeDatabaseInterface
}

define checkIsAssembleable {
    RequestResponse: getComponent( componentId )( response ) {
        httpRequest@HTTP( {
            .url = "http://localhost:8004/checkIsAssembleable/?component_id=" + componentId,
            .method = "GET"
        } )( componentId, response )
    }
}

cset {
}

execution{ concurrent }

init {
}

	

main{

    while(true){
    	[sendComponent(ComponentRequest)(response){
            foreach (component : ComponentRequest){
				checkIsAssembleable@checkIsAssembleable
    			getComponent( ComponentRequest.componentId )( response )
				println@Console("Response:" + response)()
			}
    	}]{
    		println@Console("")()
    	}
    }

}