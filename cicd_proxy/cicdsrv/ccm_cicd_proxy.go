// json.go
package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"os/exec"
	"time"
)

type BitBucketWebHkStru struct {
	Repository struct {
		Slug          string `json:"slug"`
		ID            int    `json:"id"`
		Name          string `json:"name"`
		ScmID         string `json:"scmId"`
		State         string `json:"state"`
		StatusMessage string `json:"statusMessage"`
		Forkable      bool   `json:"forkable"`
		Project       struct {
			Key         string `json:"key"`
			ID          int    `json:"id"`
			Name        string `json:"name"`
			Description string `json:"description"`
			Public      bool   `json:"public"`
			Type        string `json:"type"`
		} `json:"project"`
		Public bool `json:"public"`
	} `json:"repository"`
	RefChanges []struct {
		RefID    string `json:"refId"`
		FromHash string `json:"fromHash"`
		ToHash   string `json:"toHash"`
		Type     string `json:"type"`
	} `json:"refChanges"`
	Changesets struct {
		Size       int  `json:"size"`
		Limit      int  `json:"limit"`
		IsLastPage bool `json:"isLastPage"`
		Values     []struct {
			FromCommit struct {
				ID        string `json:"id"`
				DisplayID string `json:"displayId"`
			} `json:"fromCommit"`
			ToCommit struct {
				ID        string `json:"id"`
				DisplayID string `json:"displayId"`
				Author    struct {
					Name         string `json:"name"`
					EmailAddress string `json:"emailAddress"`
				} `json:"author"`
				AuthorTimestamp int64  `json:"authorTimestamp"`
				Message         string `json:"message"`
				Parents         []struct {
					ID        string `json:"id"`
					DisplayID string `json:"displayId"`
				} `json:"parents"`
			} `json:"toCommit"`
			Changes struct {
				Size       int  `json:"size"`
				Limit      int  `json:"limit"`
				IsLastPage bool `json:"isLastPage"`
				Values     []struct {
					ContentID     string `json:"contentId"`
					FromContentID string `json:"fromContentId"`
					Path          struct {
						Components []string `json:"components"`
						Parent     string   `json:"parent"`
						Name       string   `json:"name"`
						Extension  string   `json:"extension"`
						ToString   string   `json:"toString"`
					} `json:"path"`
					Executable       bool   `json:"executable"`
					PercentUnchanged int    `json:"percentUnchanged"`
					Type             string `json:"type"`
					NodeType         string `json:"nodeType"`
					SrcExecutable    bool   `json:"srcExecutable"`
					Links            struct {
						Self []struct {
							Href string `json:"href"`
						} `json:"self"`
					} `json:"links"`
					Properties struct {
						GitChangeType string `json:"gitChangeType"`
					} `json:"properties"`
				} `json:"values"`
				Start int `json:"start"`
			} `json:"changes"`
			Links struct {
				Self []struct {
					Href string `json:"href"`
				} `json:"self"`
			} `json:"links"`
		} `json:"values"`
		Start int `json:"start"`
	} `json:"changesets"`
}



func cicd_push_cmd(reponame string,fullbranch string,tohash string) (res bool) {
	res=false
	//app := "echo"
	app:="../script/cicdpush.sh"

	arg0 := reponame
	arg1 := fullbranch
	arg2 :=  tohash   // "\n\tfrom"
	//arg3 := "golang"

	//cmd := exec.Command(app, arg0, arg1, arg2, arg3)	
	cmd := exec.Command(app, arg0, arg1,arg2)
	fmt.Println(app)
	fmt.Println(arg0)
	fmt.Println(arg1)

	//v1
	//stdout, err := cmd.Output()
	//v2
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	err := cmd.Run()
	if err != nil {
		//log.Fatalf("cmd.Run() failed with %s\n", err)
		fmt.Println(err.Error())
		return
	}
	//fmt.Print(string(stdout))
	res =true
	return
}

func cicdwebhook_handler(w http.ResponseWriter, r *http.Request) {
	var bitbuckethook BitBucketWebHkStru
	json.NewDecoder(r.Body).Decode(&bitbuckethook)

	fmt.Println( "---->----->cicd web hook start---> ")
	dt := time.Now()
	fmt.Println("Current Date & Time: ", dt.String())
	fmt.Fprintf(w,"cicdProxy.\n")
	fmt.Fprintf(w,"reponame: %s !\n", bitbuckethook.Repository.Name)
	fmt.Printf( "reponame: %s !\n", bitbuckethook.Repository.Name)
	fmt.Fprintf(w,"branch name: %s !\n", bitbuckethook.RefChanges[0].RefID)
	fmt.Printf( "branch name: %s !\n", bitbuckethook.RefChanges[0].RefID)

	res  := cicd_push_cmd(bitbuckethook.Repository.Name,bitbuckethook.RefChanges[0].RefID,bitbuckethook.RefChanges[0].ToHash)
	fmt.Println( "push to cicd result: ", res)
	fmt.Println( "<----<----cicd web hook end-<---- ")
	fmt.Printf("\n\n\n\n\n")
}

func main() {
	http.HandleFunc("/cicdwebhook", cicdwebhook_handler)
	log.Fatal(http.ListenAndServe(":8090", nil))
}
