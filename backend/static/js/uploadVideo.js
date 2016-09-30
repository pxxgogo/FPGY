$(function(){
  var file = document.getElementById("slide_file").files[0]
  var reader = new FileReader()
  reader.readAsDataURL(file)
  reader.onload = function(event)
  {
   var result = event.target.result
   var fileName = document.getElementById("slide_file").files[0].name
   $.post("uploadVideo",
    {data: result,
    name: fileName},
    function(response_data)
	{
     if (!response_data.success)
      console.error("There was an error uploading the file", response_data)
     else
      console.log("Upload successful", response_data)
	})
  }
  reader.onloadstart = function()
  {
   console.log("onloadstart")
  }
  reader.onprogress = function(event)
  {
   console.log("onprogress", event.total, event.loaded, (event.loaded / event.total) * 100)
  }
  reader.onabort = function()
  {
   console.log("onabort")
  }
  reader.onerror = function()
  {
   console.log("onerror")
  }
  reader.onloadend = function(event)
  {
   console.log ("onloadend", event)
  }
});