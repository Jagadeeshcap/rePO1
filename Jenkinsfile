pipeline{
    agent any
    parameters{
        booleanParam(defaultValue: false,
        description: "Enable service ?",
        name:"MyBoolean")
    }
    stages{
        stage("Bulid"){
            steps{
                echo " This is Stage 1"
            }
        }
        stage("Bulid2"){
            steps{
                echo "This is stage 2"
            }
        }
        stage("Bulid2"){
            steps{
                echo "This is stage 3"
            }
        }
        stage("Bulid4"){
            steps{
                echo "This is stage 4"
            }
        }
        stage("Stage 5"){
            steps{
                echo "This is stage 5"
            }
        }
    }

}
