import React from 'react';
import './App.css';


class App extends React.Component {
  constructor(props){
    super(props);
      this.state = {
        cityList:[],
        sortedcityList:[],
        activeItem:{
          id:null, 
          title:'',
          visited:false,
        },
        editing:false,
      }
      this.fetchTasks = this.fetchTasks.bind(this)
      this.handleChange = this.handleChange.bind(this)
      this.handleSubmit = this.handleSubmit.bind(this)
      this.getCookie = this.getCookie.bind(this)


      this.startEdit = this.startEdit.bind(this)
      this.deleteItem = this.deleteItem.bind(this)
      this.strikeUnstrike = this.strikeUnstrike.bind(this)
  };

  getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

  componentWillMount(){
    this.fetchTasks()
  }

  fetchTasks(){
    console.log('Fetching...')

    fetch('http://127.0.0.1:8000/api/city-list/')
    .then(response => response.json())
    .then(data => 
      this.setState({
        cityList:data
      })
      )
    fetch('http://127.0.0.1:8000/api/results/')
    .then(response => response.json())
    .then(data => 
      this.setState({
        sortedcityList:data
      })
      )

  }

  handleChange(e){
    var name = e.target.name
    var value = e.target.value
    console.log('Name:', name)
    console.log('Value:', value)

    this.setState({
      activeItem:{
        ...this.state.activeItem,
        title:value
      }
    })
  }

  handleSubmit(e){
    e.preventDefault()
    console.log('ITEM:', this.state.activeItem)

    var csrftoken = this.getCookie('csrftoken')

    var url = 'http://127.0.0.1:8000/api/city-create/'

    if(this.state.editing == true){
      url = `http://127.0.0.1:8000/api/city-update/${ this.state.activeItem.id}/`
      this.setState({
        editing:false
      })
    }



    fetch(url, {
      method:'POST',
      headers:{
        'Content-type':'application/json',
        'X-CSRFToken':csrftoken,
      },
      body:JSON.stringify(this.state.activeItem)
    }).then((response)  => {
        this.fetchTasks()
        this.setState({
           activeItem:{
          id:null, 
          title:'',
          visited:false,
        }
        })
    }).catch(function(error){
      console.log('ERROR:', error)
    })

  }
    handleSubmitOrder(e){
    e.preventDefault()
    
  }

  startEdit(city){
    this.setState({
      activeItem:city,
      editing:true,
    })
  }
   startEdit2(city){
    this.setState({
      activeItem:city,
      editing:true,
    })
  }


  deleteItem(city){
    var csrftoken = this.getCookie('csrftoken')

    fetch(`http://127.0.0.1:8000/api/city-delete/${city.id}/`, {
      method:'DELETE',
      headers:{
        'Content-type':'application/json',
        'X-CSRFToken':csrftoken,
      },
    }).then((response) =>{

      this.fetchTasks()
    })
  }


  strikeUnstrike(city){

    city.visited = !city.visited
    var csrftoken = this.getCookie('csrftoken')
    var url = `http://127.0.0.1:8000/api/city-update/${city.id}/`

      fetch(url, {
        method:'POST',
        headers:{
          'Content-type':'application/json',
          'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'visited': city.visited, 'title':city.title})
      }).then(() => {
        this.fetchTasks()
      })

    console.log('CITY:', city.visited)
  }


  render(){
    var cities = this.state.cityList
    var sortedcities = this.state.sortedcityList

    var self = this
    return(
        <div className="container">

          <div id="city-container">
              <div  id="form-wrapper">
                 <form onSubmit={this.handleSubmit}  id="form">
                    <div className="flex-wrapper">
                        <div style={{flex: 6}}>
                            <input onChange={this.handleChange} className="form-control" id="title" value={this.state.activeItem.title} type="text" name="title" placeholder="Add city.." />
                         </div>

                         <div style={{flex: 1}}>
                            <input id="submit" className="btn btn-info" type="submit" name="Add" />
                          </div>
                      </div>
                </form>
             
              </div>

              <div  id="list-wrapper">         
                    {cities.map(function(city, index){
                      return(
                          <div key={index} className="city-wrapper flex-wrapper">

                            <div onClick={() => self.strikeUnstrike(city)} style={{flex:7}}>

                                {city.visited == false ? (
                                    <span>{city.title}</span>

                                  ) : (

                                    <strike>{city.title}</strike>
                                  )}
  
                            </div>
                            <div style={{flex:1}}>
                                <button onClick={() => self.startEdit2(city)} className="btn btn-sm btn-outline-info">-1</button>
                            </div>

                            <div style={{flex:1}}>
                                <button onClick={() => self.startEdit(city)} className="btn btn-sm btn-outline-info">Edit</button>
                            </div>

                            <div style={{flex:1}}>
                                <button onClick={() => self.deleteItem(city)} className="btn btn-sm btn-outline-dark delete">-</button>
                            </div>

                          </div>
                        )
                    })}
              </div>
          </div>
          <div id="city-container-ordered">
              <div  id="form-wrapper">
                 <form onSubmit={this.handleSubmitOrder}  id="form">
                    <div className="flex-wrapper">
                    

                         <div style={{flex: 1}}>
                            <input id="order1"  type="submit" value="Order VRP" />
                          </div>
                           <div style={{flex: 1}}>
                            <input id="order2"  type="submit" value="Display on map" />
                          </div>
                           <div style={{flex: 1}}>
                            <input id="order3"  type="submit" value="Second Best" />
                          </div>
                      </div>
                </form>
             
              </div>

              <div  id="list-wrapper-ordered">         
                    {sortedcities.map(function(city, index){
                      return(
                          <div key={index} className="city-wrapper flex-wrapper">

                            <div onClick={() => self.strikeUnstrike(city)} style={{flex:7}}>

                                {city.visited == false ? (
                                    <span>{city.title}</span>

                                  ) : (

                                    <strike>{city.title}</strike>
                                  )}
  
                            </div>
                            

                          </div>
                        )
                    })}
              </div>
          </div>
          
        </div>
      )
  }
}



export default App;