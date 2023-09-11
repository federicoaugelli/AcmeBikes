type Component: void {
     .componentId: int,
     .orderId: int
}

type ComponentRequest: void{
    .components[0, *]: Component
}

interface warehouseInterface {
     RequestResponse: sendComponent(ComponentRequest)(bool),
}