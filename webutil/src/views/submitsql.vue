<template>
	<div>
		<top></top>
		<div style="margin-top: 50px;">
		</div>
		<div style="padding: 30px;">

			<div style="text-align: right;">
				  <el-button style="width: 70px;" type="primary" @click="getinfo()">刷新</el-button>
			</div>
			<div style="display: flex;justify-content: space-between;">
				<div>
					<el-upload show-file-list="false"  class="upload-demo" drag name='files' action="http://192.168.104.117:9000/uploadsql" multiple>
						<i class="el-icon-upload"></i>
						<div class="el-upload__text">上传insertsql文件,可选择多个</em></div>
					</el-upload>
				</div>
				<div>
					<el-upload show-file-list=false class="upload-demo" drag name='filess'  action="http://192.168.104.117:9000/uploadtable"
						multiple>
						<i class="el-icon-upload"></i>
						<div class="el-upload__text">上传创表语句文件,可选择多个</em></div>
					</el-upload>
				</div>
				<div></div>
				<div></div>
			</div>
			<div style="display: flex;justify-content: space-between;margin-top: 20px;">
				<div style="margin-left: 60px;">
					已上传数据插入文件
					<div>
						<ol>
							<div v-for="item in datalist.rsqllist">
								<li>{{item}}</li>
							</div>
						</ol>
					</div>
				</div>
				<div>
					已上传建表sql文件
					<div>
						<ol>
							<div v-for="item in datalist.tablelist">
								<li>{{item}}</li>
							</div>
						</ol>
					</div>
				</div>
				<div></div>
			</div>

		</div>
		<div style="height: 100px;">

		</div>
		<foot></foot>
	</div>
</template>

<script>
	import top from '../components/top.vue'
	import foot from '../components/footer.vue'
	export default {
		name: "submitsql",
		data() {
			return {
				datalist: ''
			}
		},
		created() {
			this.getinfo()
		},
		methods: {
			on_success(){
				this.$message({
				          message: '上传成功！',
				          type: 'success'
				        });
			},
			getinfo() {
				let data = {
					da: 'null'
				}
				this.$axios.get(this.$https + "/lookinfo", this.$qs.stringify(data)).then(res => {
					console.log(res)
					this.datalist = res.data
				}).catch(res => {
					console(res)
				})
			}
		},
		components: {
			top,
			foot
		}
	}
</script>

<style>
</style>
