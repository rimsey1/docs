curl https://my.cyclr.com/api/connectors?pageSize=1000 | jq 'map({Name: .Name, Description: .Description, Icon: .Icon, Categories: .Categories, Content: .Content})'

