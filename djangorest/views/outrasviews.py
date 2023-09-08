@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todo = Todo.objects.all()
        serializer = TodoSerializers(todo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['GET', 'PUT', 'DELETE'])
def todo_mostrar_editar_deletar(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TodoSerializers(todo)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = TodoSerializers(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    def get(self, request):
        todo = Todo.objects.all()
        serializer = TodoSerializers(todo, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

        def get_objects(self, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise NotFound()
       
    def get(self, request, pk):
        todo = self.get_objects(pk)
        serializer = TodoSerializers(todo)
        return Response(serializer.data)
    
    def put(self, request, pk):
        todo = self.get_objects(pk)
        serializer = TodoSerializers(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        todo = self.get_objects(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    class ListarECriar(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

class EditarEDeletar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers   
    