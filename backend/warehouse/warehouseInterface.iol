type Component: void {
     .componentId: int,
     .orderId: int
}

type ComponentRequest: void{
    .components[0, *]: Component
}

type ComponentId: void {
     .component_id: int
}

interface warehouseInterface {
     RequestResponse: sendComponent(ComponentRequest)(bool),
}

interface AcmeDbInterface {
    RequestResponse: checkIsAssembleable(ComponentId)(int)
}